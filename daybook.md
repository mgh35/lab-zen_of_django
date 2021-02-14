### 2021-02-04

Off to an inauspicious start ...

```sh
> pyenv install 3.9.1
...
checking whether the C compiler works... no
...
```

In the end, turning it [off and on again](https://stackoverflow.com/a/64838849/11495734)
did the trick:

```sh
sudo rm -rf /Library/Developer/CommandLineTools
sudo xcode-select --install
```

For next time to start into the actual lab, then.

### 2021-02-05

I'd had in mind that this would need a frontend. (That Django would just supply the backend.) Part of the zen of Django seems to be that the Admin pages give a basic UI out the box (if users are willing to tolerate a basic UX). So running with that.

On renaming the site folder to `site` (and appropriately updating the settings path in `manage.py`) started hitting:

```sh
error: No module named 'site.settings'; 'site' is not a package)
```

Any other name seems to be fine. I guess some magic keyword somewhere. Whatever.

The apps idea is still not clear to me. The [docs](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-the-polls-app) leave me similarly confused. And other examples I've looked at least me to the issues brought up in [this](https://medium.com/@DoorDash/tips-for-building-high-quality-django-apps-at-scale-a5a25917b2b5) about apps becoming coupled. I'm going to follow that advice and keep to single-app projects. So the project folder I'll stick with `project` and the app named what I want to name it. (Admittedly, the extra level of indirection from the lab itself isn't helping.)

Levels of zen are falling quickly.

### 2021-02-06

After a losing battle, it turns out that VSCode [format on save does not to support templates](https://forum.djangoproject.com/t/automatic-formatting-of-django-templates/341). Really, prefer to keep formatting outside of the editor anyways. Turn off format on save and add precommit.

In installing pre-commit, I always forget that I need that in the dev environment, not the project environment.

### 2021-02-07

Starting to doubt the value of this lab - The only findings so far are that Django does what it does and doesn't do what it doesn't. It also depends which bit exactly one is looking at. I had in mind mainly with respect to RESTful endpoints, but my choice to use the MVT model to avoid creating a separate frontend has taken me down a separate sort of path with different considerations. I intend to quickly build the specced features and leave things at that. (Once I've finished bikeshedding and getting Bootstrap working.)

Signup is providing a challenge to the approach of keeping a single app. Particularly, the `accounts/` tree is coming out of the default auth app. But that doesn't have any signup flow. The consensus in tutorials seems to be [along the lines of this](https://levelup.gitconnected.com/how-to-implement-login-logout-and-registration-with-djangos-user-model-59442164db73). Namely, creating an `accounts` app to handle `accounts/` and have that manage the process. But there are still all the previous issues about what exactly a different app might be. Overall, opting to stick with the single-app advice. This does seem to mean moving everything into that app, though.

Discovered that moving the templates to the app, the default templates are selected unless the app appears higher in the INSTALLED_APPS list. Which then made me look at the [other auth view](https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views). Out of the box, they are the Django admin views. So kind of nice to have, but not really suitable for anything apart from an internal app. (But a nice out-of-the box feature there.) Remarkable how easy it was to follow the tutorial and not realize it was exposing this raw Django admin password reset page (presumably safe, but not something that would be wanted on a production app). I'll update to follow the approach [here](https://stackoverflow.com/questions/35153108/why-is-logged-out-html-not-overriding-in-django-registration) of explicitly taking just the links I want.


### 2021-02-09

Interest case of config and security. Using the LoginRequiredMixin, if it goes first in the class list it works as expected, but if it goes second it silently fails and unauthed users can access the page.


### 2021-02-11

Adding DRF. Mainly to see where it fits into this picture. But also, now that the /posts/ APIs are fleshed out, it's clear that they are all very similar and an abstraction like DRF would help to keep them consistent. For example, adding optional permissioned posts is going to require keeping all the views in sync. It will be interesting to see, though, if having it in DRF will allow for a seamless way to support a JSON API on the same endpoints.

It's notable that moving to DRF makes some of the common HTML interaction patterns less automated. For example, `login_required` is now gone. The template rendering also seems to require a bit of extra work (versus what was very simple in Django). But it does unify the different endpoints relating to the same model and does give a fairly seamless support for JSON or HTML.

### 2021-02-14

Another case where straying even slightly off the green path leaves you having to dig through the Django code to figure out how exactly it's doing things: Ordering is super easy - just specify the `ordering` field. But it does nothing here. Of course, the issue was that I had overridden the `get_queryset` method (so that I could apply the permission filtering). Apart from digging through the Django abstractions, not sure what the options are. To fix this case, I can 1) add ordering to my `get_queryset`, 2) have my `get_queryset` set `self.queryset` and call the base `get_queryset`, 3) because my `get_queryset` logic is just filtering, I can implement as a `filterset` instead. The latter feels like the closest way to the Django model.

I feel like that all makes sense. But for such a simple thing it requires a fairly deep understanding of the Django abstraction. Any talk of "working out the box" is wildly overstated.

Of course that was too easy. DRF changes the abstraction, and [ordering no longer works in DRF ModelView](https://stackoverflow.com/questions/24987446/django-rest-framework-queryset-doesnt-order). Again, digging into the code it's clear (`get_ordering` is overridden and doesn't implement ordering). But, come on ... So now we have to use the `OrderingFilter`.
