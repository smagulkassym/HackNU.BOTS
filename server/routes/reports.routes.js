const Router = require('express')
const reportsController = require('../controller/report.controller')
const router = new Router()

router.get('/report', reportController.getReport)

module.exports = router