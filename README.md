# hestia_certificate

Certificate Generation for Hestia

## Endpoints

### 1.Add template

```
    /add_template


    POST

    "certificate_template":<image> (only .png images)
    "event_name":<name of the event>

```

### 2.Generate Certificate

```

    /generate_certificate

    POST

    "name":<name of the person>
    "event_name":<name of the event>
    "name_x_pos":<x position of the name>
    "name_y_pos":<y pos of the name>
    "event_x_pos":<x position of the events name>
    "event_y_pos":<y position of the events name>
    "font_size":<Font size>

    The certificate file gets generated at assets/certificates/<event_name>/<name>.png
```
