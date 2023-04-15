const express = require('express')
const salesRouter = require('./routes/sales.routes')
// const suppliesRouter = require('./routes/supplies.routes')
// const reportsRouter = require('./routes/reports.routes')

require('dotenv').config();

const PORT = process.env.PORT || 5000

const app = express();

app.use(express.json());
app.use('/api', salesRouter);
// app.use('/api', suppliesRouter);
// app.use('/api', reportsRouter);

app.listen(PORT, (error) => {
    error
        ? console.log(error)
        : console.log(`The server is running in localhost:${PORT}`);
});

