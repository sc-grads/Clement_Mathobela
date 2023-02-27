visits = {'Monday': 5000,
          'Tuesday': 3000,
          'Wednesday': 4000,
          'Thursday': 4500,
          'Friday': 5000,
          'Saturday': 2000,
          'Sunday': 1500
          }

## YOUR CODE STARTS HERE
total_visits = sum(visits.values())

percentage = {k: (v / total_visits * 100) for k, v in visits.items()}