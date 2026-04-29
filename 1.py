<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>คำนวณฐานรากเยื้องศูนย์</title>
<style>
    body { font-family: Arial; margin: 20px; }
    input { width: 90px; }
    table, th, td { border: 1px solid #ccc; border-collapse: collapse; padding: 6px; }
    th { background: #eee; }
</style>
</head>
<body>

<h2>คำนวณแรงในเสาเข็ม (เยื้องศูนย์)</h2>

Q (แรงรวม): <input id="Q" type="number"><br><br>
Mx (โมเมนต์รอบแกน x): <input id="Mx" type="number"><br><br>
My (โมเมนต์รอบแกน y): <input id="My" type="number"><br><br>

จำนวนเสาเข็ม (n): <input id="n" type="number" value="2">
<button onclick="createTable()">สร้างตาราง</button>

<div id="inputTable"></div>
<br>

<button onclick="calculate()">คำนวณ</button>

<h3>ผลลัพธ์</h3>
<div id="output"></div>

<script>

function createTable(){
    let n = parseInt(document.getElementById("n").value);
    let html = "<table><tr><th>Pile</th><th>x</th><th>y</th><th>x²</th><th>y²</th></tr>";

    for(let i=0;i<n;i++){
        html += `
        <tr>
            <td>${i+1}</td>
            <td><input id="x${i}" type="number"></td>
            <td><input id="y${i}" type="number"></td>
            <td id="x2_${i}">-</td>
            <td id="y2_${i}">-</td>
        </tr>`;
    }

    html += `<tr>
        <td colspan="3"><b>รวม</b></td>
        <td id="sumx2">-</td>
        <td id="sumy2">-</td>
    </tr>`;

    html += "</table>";
    document.getElementById("inputTable").innerHTML = html;
}

function calculate(){
    let n = parseInt(document.getElementById("n").value);
    let Q = parseFloat(document.getElementById("Q").value) || 0;
    let Mx = parseFloat(document.getElementById("Mx").value) || 0;
    let My = parseFloat(document.getElementById("My").value) || 0;

    let x = [], y = [];
    let sumx2 = 0, sumy2 = 0;

    for(let i=0;i<n;i++){
        x[i] = parseFloat(document.getElementById("x"+i).value) || 0;
        y[i] = parseFloat(document.getElementById("y"+i).value) || 0;

        let x2 = x[i]*x[i];
        let y2 = y[i]*y[i];

        sumx2 += x2;
        sumy2 += y2;

        document.getElementById("x2_"+i).innerText = x2.toFixed(2);
        document.getElementById("y2_"+i).innerText = y2.toFixed(2);
    }

    document.getElementById("sumx2").innerText = sumx2.toFixed(2);
    document.getElementById("sumy2").innerText = sumy2.toFixed(2);

    let result = "<table><tr><th>Pile</th><th>Pi</th></tr>";
    let sumP = 0;

    for(let i=0;i<n;i++){
        let Pi = (Q/n);

        if(sumx2 !== 0) Pi += (My * x[i] / sumx2);
        if(sumy2 !== 0) Pi += (Mx * y[i] / sumy2);

        sumP += Pi;

        result += `<tr>
            <td>${i+1}</td>
            <td>${Pi.toFixed(2)}</td>
        </tr>`;
    }

    result += `<tr>
        <td><b>ΣPi</b></td>
        <td><b>${sumP.toFixed(2)}</b></td>
    </tr>`;

    result += "</table>";

    // ตรวจสอบสมดุล
    result += "<br><b>ตรวจสอบ:</b><br>";
    result += "ΣPi ≈ Q = " + Q;

    document.getElementById("output").innerHTML = result;
}

</script>

</body>
</html>
