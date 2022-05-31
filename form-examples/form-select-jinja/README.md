## Description

a Form that populates the values of the dropdown with the values that is passed via the `render_template` function.

The jinja template uses a for loop to loop through all the `countries` and then populates the select fields:

```
...
    <div class="form-group">
        <label for="countryName">Country Name</label>
        <select class="custom-select" name="countryName" id="countryNameId">
          {% for country in countries %}
          <option value="{{ country }}">{{ country }}</option>
          {% endfor %}
        </select>
    </div>
...
```
