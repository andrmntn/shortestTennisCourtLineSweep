# Shortest Tennis Court Line Sweep

---
If you play Tennis regularly, you can probably relate. You are sweeping the Court and are doing the lines, when you stop and ask yourself for a split-second, what the fastest and most efficent way would be to clean the lines. I recently asked myself the same question and decided to write a short script to calculate the shortest path.
I modeled the tennis court as an undirected, weighted graph as follows:
Link to Online Graph Design: https://graphonline.ru/en/?graph=WWYHrfMYOVEHUYmY

<img width="400" alt= "Tennis Court modeled as a Graph" src="https://github.com/andrmntn/shortestTennisCourtLineSweep/assets/54849338/891faa13-17dc-4b91-a072-4924835328b5">




I came to the conclusion that the fastest path with minimal wasted distance looks as follows:
<img width="400" alt="optimal walking path" src="https://github.com/andrmntn/shortestLineSweep/assets/54849338/e89fe928-c21b-4a30-b5e7-8402addf6435">


The minimal wasted distance is 8.21 Meters

Feel free to use my simple code for arbitrary graphs. :)
