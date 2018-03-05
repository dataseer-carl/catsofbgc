# catsofbgc
#catsofbgc

# project-name
Short description from GitHub

## Data dump

Location of `data://` [here](https://goo.gl/d6MPss).

## Data sources

### Raw
Raw data files.

| Data File/Directory | Description | Location | Columns | Rows | Size |
|:--|:--|:--|--:|--:|--:|

### Loaded
Parsed data files.

| Dataset | Data File | Description | Columns | Rows | Input Data | Data Processing Scripts |
|:--|:--|:--|--:|--:|:--|:--|
| Raw IG data | `ig raw.json` | Raw IG data as of 2018-03-02 |  |  |  | `ig_cats.py` |
| Shortlisted IG data | `cats_of_bgc.h5` | IG data with shortlisted columns as of 2018-03-02 |  |  |  | `ig_cats.py` |
| Raw Twitter data | `twitter_raw.json` | Raw Twitter data as of 2018-03-02 |  |  |  | `twitter_cats.py` |

## Work Products

#### Data

| Data File | Description | Columns | Rows | Input Data | Data Processing Scripts | csv Data File | xlsx Data File | R Data File |
|:--|:--|--:|--:|:--|:--|:--|:--|:--|
| `main_df.json` | Consolidated raw IG and raw Twitter data |  |  | `ig raw.json`<br/>`twitter_raw.json` | `social_media.py` |  |  |  |

#### Plots

| Plot | File | Script | Input data |
|:--|:--|:--|:--|

#### Dashboards

| Dashboard | Platform | Location | Input data |
|:--|:-:|:--|:--|

#### Models

#### Reports
