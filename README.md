# GALAH File Read Testing

A few basic functions and notebooks where I attempt to:

1. Get a list of [GALAH objects](https://www.galah-survey.org/dr3/the_spectra/#downloading-the-spectra-for-a-few-stars) via the Data Central API 
2. Use the `sobject_id`s to get their spectral data in fits format by passing onto another set of functions.

Adapted from the excellent [Sven Buder](https://github.com/svenbuder/GALAH_DR3/blob/master/tutorials/tutorial3_plotting_reduced_spectra.ipynb) and [Brent Miszalski](https://docs.datacentral.org.au/help-center/virtual-observatory-examples/ssa-galah-dr3-interactive-spectra-explorer-enhanced-data-central-api/)

The Data Central API has a hard limit of 1000 objects you can query via the methods in galah-test-read-praveen.ipynb so if you want a longer list of `sobject_ids` I recommend writing a query via the [web interface](https://datacentral.org.au/api/services/query/) and waiting for the result to appear in your inbox. The email will have a link to the query result which you can then download into a format of your choice e.g. csv, VO, fits etc. 

For all activities, I recommend opening a [Data Central](https://datacentral.org.au/) account. 