const Router = require('express')
const reportController = require('../controller/report.controller')
const router = new Router()

router.get('/reports', reportController.getReport)

module.exports = router