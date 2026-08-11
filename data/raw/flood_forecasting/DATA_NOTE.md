# Updated flood forecasting dataset

The forecasting dataset was regenerated at the target-label stage.

For each synthetic station, the flood danger level is defined as the
90th percentile of its simulated 6-hour-ahead water-level distribution.
Therefore, flood events occur in roughly the upper 10% of conditions
rather than only during a tiny number of extreme spikes.

This is still SYNTHETIC data. The threshold is a modeling assumption,
not an official river danger level.

The underlying temporal relationship remains:
rainfall -> soil moisture -> discharge -> water level -> future flood.
