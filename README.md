#Django-Drupal Password Hasher

## Introduction

Django-Drupal Password Hasher is a simple package created to hash Drupal 7 passwords with the prefix 'drupal'

## Installation

In your virtualenv

    pip install Django-Drupal-Password-Hasher     

In your .py file

    from djangodrupalpasswordhasher import drupal_password_hasher

Add the following line to your settings.py file in the "PASSWORD_HASHERS" section

    'djangodrupalpasswordhasher.drupal_password_hasher.DrupalPasswordHasher',
