# Lab: Zen of Django

What is the zen of Django?

## Introduction

The point of this lab is to try to find the zen of Django. Particularly, as I am
starting to work with Django I find myself fighting against the machine rather than
being able to take advantage of it. I hope to explore a central use-case to
discover where the power of the platform lies.

The major hurdles I find getting into the platform are:

- Active Record Pattern ORM. It is a confusing model for the unitiate. Particularly when
  used to analytics-type query, things like the inability express queries outside the
  model is frustrating.
- Very heavy framework. If you find yourself trying to do something against its grain,
  it is an uphill battle that the framework will win.
- Auth. The focus on object IDs is confusing when approached from a different context.
- Configuration over code. Even harder with an untyped language.

Many of these sound like a problem of approaching this without having previously built
many CRUD-type apps. (Or possibly, without having understood that other problems were in
fact CRUD-type problems.)

So building this little app is intended to give a sense of developing in Django going
with its grain. The natural place to start is the sort of thing along the lines for
which Django was created. To that end, the idea is to build out a blog site.

## App Spec

This app is a simple blog site. Users should be able to:

- View public posts and comments.
- Publish comments to posts with public comments enabled.
- Create an account, log in, log out.
- Publish posts, with selectable visibility, when logged in.
- Publish comments on posts with restricted comments enabled when authorized.
- Follow other users.
