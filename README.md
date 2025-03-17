# Case

## Power supplier
A power-station has a water reservoir that can be used to generate electricity. The water reservoir is filled by rain and it has a constant upstream water supply. 
This means, if you do not adjust anything, the power-station will generate electricity at a constant rate of `20 MW`.
The Water level in the reservoir is measured in meters and the power-station can generate electricity at a rate of `1 MW` for every `1 meter` of water in the reservoir.
At the current moment the reservoir is `100 meters` and the upstream water supply provides `30 meters` of water every hour.

It is your job to adjust how much power the power-station produces every hour based on the water level in the reservoir. And it should be optimized in such a way that the power-station generates as much power as possible based on the data matrix provided in the `.csv` file.


### Dateframe with data
```python
>>> import pandas
>>> df = pandas.read_csv('data.csv')
>>> df
     Hour   0   1   2   3   4   5   6   7   8   9   10
0   00:00  20  25  30  35  40  45  50  55  60  70   80
1   01:00  20  25  30  35  40  45  50  55  60  70   80
2   02:00  20  22  25  30  35  40  45  50  60  70   80
3   03:00  20  22  25  30  35  40  45  50  60  70   80
4   04:00  20  22  25  30  35  40  45  50  60  70   80
5   05:00  20  25  30  35  40  45  50  55  60  75   90
6   06:00  20  35  40  50  60  70  75  80  85  90  100
7   07:00  20  45  50  60  70  80  85  90  95  98  100
8   08:00  20  55  60  70  80  85  90  95  98  99  100
9   09:00  20  45  50  60  70  75  80  85  90  95  100
10  10:00  20  40  45  55  65  70  75  80  85  90  100
11  11:00  20  35  40  50  60  65  70  75  80  90  100
12  12:00  20  35  40  50  60  65  70  75  80  85  100
13  13:00  20  30  35  45  55  60  65  70  75  85  100
14  14:00  20  25  30  40  50  55  60  65  70  80  100
15  15:00  20  25  30  40  50  55  60  65  70  80  100
16  16:00  20  30  35  45  55  60  65  70  75  85  100
17  17:00  20  40  45  55  65  70  75  80  85  95  100
18  18:00  20  55  60  70  80  85  90  95  98  99  100
19  19:00  20  55  60  70  80  85  90  95  98  99  100
20  20:00  20  45  50  60  70  75  80  85  90  95  100
21  21:00  20  35  40  50  60  65  70  75  80  90  100
22  22:00  20  25  30  40  50  55  60  65  70  85  100
23  23:00  20  25  30  40  50  55  60  65  70  85  100

>>>
```

For every hour you can adjust the power output levels 0-10 to meet the MW demand for each hour. The higher the output level the more water you use from the reservoir.
You can save water for a later hour, but you can not use more water than the reservoir can hold. The reservoir can hold `100 meters` of water.
Given this matrix, what is the optimal power output levels for each hour to maximize the power generated?

Example: at `00:00` you can choose to produce `40 MW` and draining `40 meters` of water from the reservoir. This will leave you with `60 meters` of water in the reservoir. But since the upstream fills the reservoir with `30 meters` every hour, you will have `90 meters` of water at `01:00`. This means you can produce `90 MW` at `01:00` and so on.

PS: You can drain the reservoir to `0 meters` if you want to, and optimally you should expect to have `0 meters` of water in the reservoir at `23:00`.

Present your solution using code and explain your reasoning. We are looking for how you approach the problem and how you solve it, not just the solution itself.

Example of unoptimized solution:
```python
power_levels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
```
This gives a total of 10, but it is not optimal because you keep overflowing the reservoir and wasting resources.
The `main.py` module has code and asserts to showcase valid and optimial solutions. You need to find any other or better.

## Part 2 Variables

In the future we want this task to account for variables in live weather data from yr.no. if it rains in the next 24 hours, this will change the upstream water amount positive.

Please explain how you would implement this in your solution. No code is needed for this part.

## Part 3 - Real data

This example is greatly simplified. The provided raw data is based on a real dataset, from one reactor, from one location during one day. Given that the real data is based on bid price, and not `MW` and `water in meters`, how would you change your approach.

# Setup intructions.

You need `uv` installed. 

## macos and linux: 
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


## Windows
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Better alternative with pipx or homebrew
better alternative is to get it from pypi with `pipx`

```bash
pipx install uv
```
or
```bash
brew install uv
```

## Clone and install:

