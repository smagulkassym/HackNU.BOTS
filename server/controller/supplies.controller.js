const db = require('../db');

class SuppliesController{
    // async getSupply(req, res) {
    //     const id = req.params.id
    //     res.json(`ok ${id}`) // test this
    // }
    
    async getSupplies(req, res) {
        const barcode = req.query.barcode;
        const fromTime = req.query.fromTime;
        const toTime = req.query.toTime;
        const supplies = await db.query(`SELECT * FROM umag_hacknu.supply WHERE barcode = '${barcode}' 
                                                AND supply_time >= '${fromTime}' 
                                                AND supply_time <= '${toTime}'`)
        res.json(supplies.rows)
    }
    

    async getSupply(req, res) {
        const id = req.params.id
        const supply = await db.query(`SELECT * FROM umag_hacknu.supply WHERE id = '${id}'`)
        res.json(supply.rows) // test this
    }

    async createSupply(req, res) {
        const {barcode, price, quantity, supplyTime} = req.body

        console.log(`${barcode}, ${price}, ${quantity}, ${supplyTime}`);

        const newSupply = await db.query(`
            INSERT INTO umag_hacknu.supply 
                (id, barcode, price, quantity, supply_time)
            VALUES 
                (DEFAULT, $1, $2, $3, $4)
            RETURNING id`,
            [barcode, price, quantity, supplyTime]
            );

        res.json(newSupply.rows[0]) // works ok
        
    }

    async editSupply(req, res) {
        const id = req.params.id
        const {barcode, price, quantity, supplyTime} = req.body
        const supply = await db.query(`
            UPDATE umag_hacknu.supply
            SET barcode = '${barcode}', 
                price = '${price}', 
                quantity = '${quantity}', 
                supply_time = '${supplyTime}'
            WHERE id = '${id}'
        `)
        
        res.json(supply.rows[0]) // works ok
        // res.json(supply.rows)
    }

    async deleteSupply(req, res) {
        const id = req.params.id
        const supply = await db.query(`DELETE FROM umag_hacknu.supply WHERE id = '${id}'`)
        res.json(supply.rows[0]) // test this
    }
}

module.exports = new SuppliesController()