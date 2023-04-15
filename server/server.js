const express = require('express')
const salesRouter = require('./routes/sales.routes')
const suppliesRouter = require('./routes/supplies.routes')
const reportsRouter = require('./routes/reports.routes')

const PORT = 3000;

const app = express()

app.use('/api', salesRouter);
app.use('/api', suppliesRouter);
app.use('/api', reportsRouter);

app.listen(PORT, (error) => {
    error
        ? console.log(error)
        : console.log(`The server is running in localhost:${PORT}`);
});

