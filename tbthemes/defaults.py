"""Einstellungen für Social Media Links, die via Admin bearbeitet werden können"""
from mezzanine.conf import register_setting

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=("Sequence of setting names available within templates."),
    editable=False,
    default=("SOCIAL_LINK_FACEBOOK", "SOCIAL_LINK_VIMEO",
             "SOCIAL_LINK_TWITTER", "SOCIAL_LINK_INSTAGRAM", "FLICKR_ID"),
    append=True,
)

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=("Facebook link"),
    description=("If present a Facebook icon linking here will be in the "
        "header."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_VIMEO",
    label=("Vimeo link"),
    description=("If present a vimeo icon linking here will be in the "
        "header."),
    editable=True,
    default="https://vimeo.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=("Twitter link"),
    description=("If present a twitter icon linking here will be in the "
        "header."),
    editable=True,
    default="https://twitter.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_INSTAGRAM",
    label=("Instagram link"),
    description=("If present a Instragram icon linking here will be in the "
        "header."),
    editable=True,
    default="https://instagram.com/mezzatheme",
)

register_setting(
    name="FLICKR_ID",
    label=("Flickr ID"),
    description=("ID of current Flickraccount."),
    editable=True,
    default="",
)
