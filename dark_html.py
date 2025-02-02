def serve_html():
    return """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ride Statistics</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

            body {
                font-family: 'Montserrat', sans-serif;
                background-image: url('https://i.ibb.co/TmTr6Qn/1726886922384.png');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                color: #f0f0f0;
            }

            .container {
                background-color: rgba(0, 0, 0, 0.3);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
                text-align: center;
                max-width: 600px;
                width: 100%;
            }

            h1 {
                font-size: 2.5em;
                margin-bottom: 30px;
                position: relative;
                padding-bottom: 10px;
            }

            h1:after {
                content: "";
                position: absolute;
                left: 50%;
                bottom: 0;
                transform: translateX(-50%);
                width: 50px;
                height: 3px;
                background-color: #4CAF50;
            }

            .card {
                background-color: #222;
                border: 1px solid #333;
                border-radius: 15px;
                padding: 20px;
                margin: 20px 0;
                transition: transform 0.2s, box-shadow 0.2s;
            }

            .card:hover {
                transform: scale(1.05);
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
            }

            .card i {
                font-size: 40px;
                color: #4CAF50;
                margin-bottom: 10px;
            }

            h2 {
                color: #f0f0f0;
                font-size: 1.5em;
                margin-bottom: 10px;
            }

            p {
                font-size: 24px;
                color: #ccc;
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
