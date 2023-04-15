const Router = require('express')
const salesController = require('../controller/sales.controller')
const router = new Router()

router.get('/sales', salesController.getSales)
router.get('/sales/:id', salesController.getSale)
router.post('/sales', salesController.createSale)
router.put('/sales/:id', salesController.editSale)
router.delete('/sales/:id', salesController.deleteSale)


module.exports = router