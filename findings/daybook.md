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

I'd had in mind that this would need a frontend. (That Django would just supply the
backend.) Part of the zen of Django seems to be that the Admin pages give a basic UI
out the box (if users are willing to tolerate a basic UX). So running with that.

On renaming the site folder to `site` (and appropriately updating the settings path
in `manage.py`) started hitting:

```sh
error: No module named 'site.settings'; 'site' is not a package)
```

Any other name seems to be fine. I guess some magic keyword somewhere. Whatever.

The apps idea is still not clear to me. The [docs](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-the-polls-app) leave me similarly confused. And other examples I've looked at least me to the issues brought up in [this](https://medium.com/@DoorDash/tips-for-building-high-quality-django-apps-at-scale-a5a25917b2b5) about apps becoming coupled. I'm going to follow that advice and keep to single-app projects. So the project folder I'll stick with `project` and the app named what I want to name it. (Admittedly, the extra level of indirection from the lab itself isn't helping.)

Levels of zen are falling quickly.

### 2021-02-06

After a losing battle, it turns out that VSCode [format on save does not to support templates](https://forum.djangoproject.com/t/automatic-formatting-of-django-templates/341). Really, prefer to keep formatting outside of the editor anyways. Turn off format on save and add precommit.

In installing pre-commit, I always forget that I need that in the dev environment, not
the project environment.
