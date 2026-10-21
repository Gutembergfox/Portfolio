# Source, attribution and reuse

Fanaee-T, H. (2013). **Bike Sharing** [Dataset]. UCI Machine Learning Repository. DOI: [10.24432/C5W894](https://doi.org/10.24432/C5W894).

- [Official dataset page](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)
- [Official download](https://archive.ics.uci.edu/static/public/275/bike%2Bsharing%2Bdataset.zip)
- License displayed on the UCI page when checked on **21 October 2026**: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).
- The source contains Capital Bikeshare rental counts for 2011–2012 with weather and calendar information.
- Only `day.csv` is redistributed here. It was extracted unchanged from the official ZIP; the hourly file is not included.
- See [source.json](source.json) for exact download and extracted-file SHA-256 checksums.

Derived CSV summaries and charts are new aggregations of these data. They do not imply endorsement by the dataset creator, UCI or Capital Bikeshare. The attribution above applies to the dataset, not a new license on the entire repository.

The pipeline uses date, year, day-type, weather category and rental counts. `workingday=1` means neither weekend nor holiday; `cnt` is the sum of casual and registered rental counts. Weather codes are: 1 clear/few clouds, 2 mist/cloudy, 3 light snow/rain-related conditions, 4 severe rain/snow-related conditions. See the official page for the full definitions. Weather codes are categories, not a numerical severity score used in a regression here.
