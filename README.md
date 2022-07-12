# wkhtmltoimage-action
Github Action to get screenshots of a list of URLs/(sub)domains.

Example Usage
-----

**GitHub Action running wkhtmltoimage on list of hosts**

```yaml
      - name: wkhtmltoimage
        uses: huseinayub/wkhtmltoimage-action@v1
        with:
          list: hosts.txt
```


**Example workflow**: `.github/workflows/wkhtmltoimage-action.yml`


```yaml
name: wkhtmltoimage

on:
    schedule:
      - cron: '0 0 * * *'
    workflow_dispatch:

jobs:
  wkhtmltoimage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: wkhtmltoimage
        uses: huseinayub/wkhtmltoimage-action@v1
        with:
          list: hosts.txt
  
```
## Credits to:

This action is based on https://github.com/jarrekk/imgkit & https://wkhtmltopdf.org & https://hub.docker.com/r/surnet/alpine-python-wkhtmltopdf to render HTML into PDF and various image formats. Please feel free to fork this action and tweak it the way you need to upload the generated image to a location/service of your choice :)