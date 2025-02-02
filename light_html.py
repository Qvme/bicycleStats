def serve_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ride Statistics</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background-color: #f0f8ff;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        h1 {
            color: #ff6f61;
            font-size: 2.5em;
        }

        .card {
            background: #ffe4e1;
            border: 1px solid #ffb6c1;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            transition: transform 0.2s, box-shadow 0.2s;
            position: relative;
        }

        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
        }

        .card i {
            font-size: 40px;
            color: #ff6f61;
            margin-bottom: 10px;
        }

        h2 {
            color: #ff69b4;
            font-size: 1.5em;
        }

        p {
            font-size: 28px;
            color: #555;
            margin: 0;
        }
    </style>
    <script>
        function updateStats() {
            fetch('/stats')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('total_rides').innerText = data.total_rides;
                    document.getElementById('total_riding_time').innerText = data.total_riding_time + ' secs';
                    document.getElementById('total_distance').innerText = data.total_distance + ' meters';
                })
                .catch(error => console.error('Error fetching stats:', error));
        }
        setInterval(updateStats, 5000); // Update every 5 seconds
    </script>
</head>
<body>
    <div class="container">
        <h1>🚴 Ride Statistics</h1>
        <div class="card">
            <i class="fas fa-bicycle"></i>
            <h2>Total Rides</h2>
            <p id="total_rides">0</p>
        </div>
        <div class="card">
            <i class="fas fa-clock"></i>
            <h2>Total Riding Time</h2>
            <p id="total_riding_time">0 secs</p>
        </div>
        <div class="card">
            <i class="fas fa-road"></i>
            <h2>Total Distance</h2>
            <p id="total_distance">0 meters</p>
        </div>
    </div>
</body>
</html>
"""