import authomatic

CONFIG = {

    #===========================================================================
    # Defaults
    #===========================================================================

    '__defaults__': { # This is an optional special item where you can define default values for all providers.
         # You can override each default value by specifying it in concrete provider dict.
         'sreg': ['fullname', 'country'],
         'pape': ['http://schemas.openid.net/pape/policies/2007/06/multi-factor'],
    },

    #===========================================================================
    # OAuth 2.0
    #===========================================================================

    'facebook': { # Provider name.
         'class_': 'authomatic.providers.oauth2.Facebook',  # Provider class. Don't miss the trailing underscore!

         # Provider type specific keyword arguments:
         'short_name': 1, # Unique value used for serialization of credentials only needed by OAuth 2.0 and OAuth 1.0a.
         'consumer_key': '1736039409960890', # Key assigned to consumer by the provider.
         'consumer_secret': '70881d2b7fdae686b7e64946f34556d1', # Secret assigned to consumer by the provider.
         'scope': ['user_about_me', # List of requested permissions only needed by OAuth 2.0.
                   'email', 'publish_stream']
    }
}