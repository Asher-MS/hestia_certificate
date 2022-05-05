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
    "name_box_height":<height of the name box>
    "name_box_width":<width of the name box>
    "event_x_pos":<x position of the events name>
    "event_y_pos":<y position of the events name>
    "event_box_height":<height of the event box>
    "event_box_width":<width of the event box>
    "font_family":<The Font family of the text> Choices : [albertus,montserrat,tapestry,formata]

    The certificate file gets generated at assets/certificates/<event_name>/<name>.png
```

### List Certificates

```
    /list_certificates?event=<event name>

    GET
    if event is not provided returns all the certificats present in the server
    if event is provided returns all the certificates of the specific event
```
