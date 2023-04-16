const{ spawn } = require('child_process');

class ReportController{
    async getReport(req, res) {
        const barcode = req.query.barcode;
        const fromTime = req.query.fromTime;
        const toTime = req.query.toTime;

        const pythonScript = spawn('python3', ['./scripts/test.py']);
        
        pythonScript.stdin.write(`${barcode}\n`);
        pythonScript.stdin.write(`${fromTime}\n`);
        pythonScript.stdin.write(`${toTime}\n`);

        pythonScript.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`);
            const response = JSON.parse(data.toString());
            const report = {
                "barcode": response.barcode,
                "quantity": response.quantity,
                "revenue": response.revenue,
                "netProfit": response.netProfit
            }
            res.json(report);
        });

        pythonScript.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
        });

        pythonScript.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
        });

    }
}

module.exports = new ReportController()