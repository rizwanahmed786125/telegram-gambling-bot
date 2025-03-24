<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pi Token Price Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        input { padding: 10px; margin: 10px; width: 200px; font-size: 18px; }
        button { padding: 10px; font-size: 18px; cursor: pointer; }
        #result { margin-top: 20px; font-size: 22px; font-weight: bold; }
    </style>
</head>
<body>
    <h2>Pi Token Price Calculator</h2>
    <p>Enter the number of Pi tokens:</p>
    <input type="number" id="piTokens" placeholder="Enter Pi tokens">
    <button onclick="calculatePrice()">Calculate</button>
    <p id="result"></p>

    <script>
        function calculatePrice() {
            const gcbPrice = 314159; // gCB value in USD
            let piTokens = document.getElementById("piTokens").value;
            let price = piTokens * gcbPrice;
            document.getElementById("result").innerHTML = `Your Pi tokens are worth: $${price.toLocaleString()}`;
        }
    </script>
</body>
</html>
