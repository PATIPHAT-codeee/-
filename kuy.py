<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>คำนวณฐานรากเยื้องศูนย์</title>
<style>
    body { font-family: Arial; margin: 20px; }
    input { width: 80px; margin: 5px; }
    table, th, td { border: 1px solid #ccc; border-collapse: collapse; padding: 5px; }
    canvas { border:1px solid #000; margin-top:20px;}
</style>
</head>
<body>

<h2>คำนวณแรงในเสาเข็ม (เยื้องศูนย์)</h2>

Q: <input id="Q" type="number"><br>
Mx: <input id="Mx" type="number"><br>
My: <input id="My" type="number"><br>
จำนวนเสาเข็ม (n): <input id="n" type="number" value="2"><br><br>

<button onclick="generate()">สร้างตาราง</button>

<div id="tableArea"></div>
<br>
<button onclick="calculate()">คำนวณ</button>

<h3>ผลลัพธ์</h3>
<div id="result"></div>

<canvas id="canvas" width="400" height="400"></canvas>

<script>

function generate(){
    let n = document.getElementById("n").value;
    let html = "<table><tr><th>Pile</th><th>x</th><th>y</th></tr>";
    
    for(let i=0;i<n;i++){
        html += `<tr>
            <td>${i+1}</td>
            <td><input id="x${i}" type="number"></td>
            <td><input id="y${i}" type="number"></td>
        </tr>`;
    }
    html += "</table>";
    document.getElementById("tableArea").innerHTML = html;
}

function calculate(){
    let n = parseInt(document.getElementById("n").value);
    let Q = parseFloat(document.getElementById("Q").value);
    let Mx = parseFloat(document.getElementById("Mx").value);
    let My = parseFloat(document.getElementById("My").value);

    let sumx2 = 0, sumy2 = 0;
    let x = [], y = [];

    for(let i=0;i<n;i++){
        x[i] = parseFloat(document.getElementById("x"+i).value);
        y[i] = parseFloat(document.getElementById("y"+i).value);
        sumx2 += x[i]*x[i];
        sumy2 += y[i]*y[i];
    }

    let output = "<table><tr><th>Pile</th><th>Pi</th></tr>";

    for(let i=0;i<n;i++){
        let Pi = (Q/n) + (My * x[i] / sumx2) + (Mx * y[i] / sumy2);
        output += `<tr><td>${i+1}</td><td>${Pi.toFixed(2)}</td></tr>`;
    }

    output += "</table>";
    document.getElementById("result").innerHTML = output;

    draw(x,y);
}

function draw(x,y){
    let canvas = document.getElementById("canvas");
    let ctx = canvas.getContext("2d");

    ctx.clearRect(0,0,400,400);

    // origin
    let cx = 200, cy = 200;

    // draw axis
    ctx.beginPath();
    ctx.moveTo(0,200);
    ctx.lineTo(400,200);
    ctx.moveTo(200,0);
    ctx.lineTo(200,400);
    ctx.stroke();

    for(let i=0;i<x.length;i++){
        let px = cx + x[i]*20;
        let py = cy - y[i]*20;

        ctx.beginPath();
        ctx.arc(px,py,5,0,2*Math.PI);
        ctx.fill();

        ctx.fillText("P"+(i+1), px+5, py-5);
    }
}

</script>

</body>
</html>
