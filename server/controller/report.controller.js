const{ spawn } = require('child_process');

class ReportController{
    async getReport(req, res) {
        const barcode = req.query.barcode;
        const fromTime = req.query.fromTime;
        const toTime = req.query.toTime;

        // const barcode = '123123';
        // const fromTime = 666666;
        // const toTime = 999999;

        const pythonScript = spawn('python3', ['./scripts/test.py']);

        pythonScript.stdin.write(`${barcode}\n`);
        pythonScript.stdin.write(`${fromTime}\n`);
        pythonScript.stdin.write(`${toTime}\n`);

        pythonScript.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`);
            const response = JSON.parse(data.toString());
            const report = {
                "barcode": response.barcode,
                "fromTime": response.fromTime,
                "toTime": response.toTime
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