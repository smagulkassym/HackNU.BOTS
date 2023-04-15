const express = require('express')

const PORT = 3000;

const app = express()

app.listen(PORT, (error) => {
    error
        ? console.log(error)
        : console.log(`The server is running in localhost:${PORT}`);
});

