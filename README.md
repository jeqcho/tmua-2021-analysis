# Analysis of Test of Mathematics for University Admission (TMUA) 2021

From the [PDF](https://www.admissionstesting.org/Images/640676-tmua-explanation-of-results-2021.pdf) of Cambridge Assessment Admission Testing.
> Results for TMUA are reported on a scale that runs from 1 (low) to 9 (high), with scores being reported to one decimal place.
The scale has been designed so that approximately one third of candidates will achieve overall scores higher than 6.5. High scores are capped at 9.0.
The distribution of the 2021 TMUA scores, overall and for Papers 1 and 2 are shown below.

The figure shows the distribution of the grades. However, I am interested in the exact cutoff of the cumulative percentage of each grade. The results are as follows

## TMUA 2021 Overall Grade Boundaries (Cumulative)

| Grade      | Cumulative percentage |
| ----------- | ----------- |
| 1.0 | 1.62%   |
| 1.1 | 2.72%   |
| 1.5 | 4.45%   |
| 1.9 | 6.89%   |
| 2.3 | 9.75%   |
| 2.6 | 13.26%  |
| 3.0 | 17.59%  |
| 3.3 | 22.23%  |
| 3.6 | 27.32%  |
| 3.9 | 32.33%  |
| 4.2 | 37.72%  |
| 4.5 | 42.84%  |
| 4.8 | 48.40%  |
| 5.1 | 52.59%  |
| 5.4 | 58.06%  |
| 5.6 | 63.42%  |
| 5.9 | 67.93%  |
| 6.2 | 72.30%  |
| 6.5 | 75.54%  |
| 6.6 | 78.56%  |
| 6.7 | 82.03%  |
| 6.8 | 85.30%  |
| 7.0 | 88.16%  |
| 7.1 | 90.30%  |
| 7.2 | 92.39%  |
| 7.4 | 94.15%  |
| 7.5 | 95.55%  |
| 7.7 | 96.59%  |
| 7.9 | 97.56%  |
| 8.1 | 98.32%  |
| 8.3 | 98.73%  |
| 8.6 | 99.28%  |
| 9.0 | 100.00% |

## TMUA 2021 Paper 1 Grade Boundaries (Cumulative)

| Grade      | Cumulative percentage |
| --- | ------- |
| 1.0 | 4.99%   |
| 1.9 | 10.40%  |
| 2.6 | 17.11%  |
| 3.3 | 24.83%  |
| 3.9 | 33.24%  |
| 4.5 | 43.77%  |
| 5.0 | 55.06%  |
| 5.6 | 63.65%  |
| 6.1 | 71.41%  |
| 6.6 | 79.04%  |
| 6.8 | 84.95%  |
| 7.0 | 89.74%  |
| 7.3 | 93.58%  |
| 7.6 | 96.15%  |
| 7.9 | 97.85%  |
| 8.3 | 98.88%  |
| 9.0 | 100.00% |

## TMUA 2021 Paper 2 Grade Boundaries (Cumulative)

| Grade      | Cumulative percentage |
| --- | ------- |
| 1.0 | 2.86%   |
| 1.1 | 5.98%   |
| 1.9 | 11.48%  |
| 2.7 | 19.23%  |
| 3.3 | 27.79%  |
| 3.9 | 37.24%  |
| 4.5 | 46.63%  |
| 5.1 | 56.83%  |
| 5.7 | 64.64%  |
| 6.3 | 71.81%  |
| 6.7 | 79.01%  |
| 6.8 | 84.69%  |
| 7.2 | 89.70%  |
| 7.5 | 93.56%  |
| 7.8 | 96.42%  |
| 8.3 | 98.42%  |
| 9.0 | 100.00% |

## How does it work?
I extracted the images from PDF using [ilovepdf](https://www.ilovepdf.com/pdf_to_jpg).
Using [Pillow](https://pillow.readthedocs.io/), I calculated the number of pixels similar to the colour of the light blue used inside the plots RGB(189, 215, 239) with a tolerance value of 100. Lower tolerance values failed because of the JPG nature of the images cause a splatter of colours near the edge of the bars. You can see these failures colourised at the [failed-tolerances](https://github.com/jeqcho/tmua-2021-analysis/tree/master/failed-tolerances) folder. Main code is in main.py.

Inspired by my maths teacher Ms Wei Yee.
Enjoy! Contact: chooijqweb@gmail.com