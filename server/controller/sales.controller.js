const db = require('../db');

class SalesController{
    // async getSale(req, res) {
    //     const id = req.params.id
    //     res.json(`ok ${id}`) // test this
    // }
    
    async getSales(req, res) {
        const barcode = req.query.barcode;
        const fromTime = req.query.fromTime;
        const toTime = req.query.toTime;
        const sales = await db.query(`SELECT * FROM umag_hacknu.sale WHERE barcode = '${barcode}' 
                                                AND sale_time >= '${fromTime}' 
                                                AND sale_time <= '${toTime}'`)
        res.json(sales.rows)
    }
    

    async getSale(req, res) {
        const id = req.params.id
        const sale = await db.query(`SELECT * FROM umag_hacknu.sale WHERE id = '${id}'`)
        res.json(sale.rows) // test this
    }

    async createSale(req, res) {
        const {barcode, price, quantity, saleTime} = req.body

        console.log(`${barcode}, ${price}, ${quantity}, ${saleTime}`);

        const newSale = await db.query(`
            INSERT INTO umag_hacknu.sale 
                (id, barcode, price, quantity, sale_time)
            VALUES 
                (DEFAULT, $1, $2, $3, $4)
            RETURNING id`,
            [barcode, price, quantity, saleTime]
            );

        res.json(newSale.rows[0]) // works ok
        
    }

    async editSale(req, res) {
        const id = req.params.id
        const {barcode, price, quantity, saleTime} = req.body
        const sale = await db.query(`
            UPDATE umag_hacknu.sale
            SET barcode = '${barcode}', 
                price = '${price}', 
                quantity = '${quantity}', 
                sale_time = '${saleTime}'
            WHERE id = '${id}'
        `)
        
        res.json(sale.rows[0]) // works ok
        // res.json(sale.rows)
    }

    async deleteSale(req, res) {
        const id = req.params.id
        const sale = await db.query(`DELETE FROM umag_hacknu.sale WHERE id = '${id}'`)
        res.json(sale.rows[0]) // test this
    }
}

module.exports = new SalesController()