# thoughtful

## How to Run:
Import the function to your file and pass the arguments to the function as you want, like below:
sort(width, height, length, mass)

```
from robot_arm import sort

sort(100, 100, 100, 10)
```

## How to Run tests:

Install pytest dependency:
```pip install -r requirements.txt```

Now run pytest pointing to the test file:
```pytest -v test_robot_arm.py```