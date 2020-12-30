# bestow

a wrapper for GNU stow to enable some goodies.

## Goals

1. Allow environment variables in content
2. Allow changing stow target directories

### Terminology

**stow** - GNU stow utility
**package** - a directory being stowed
**meta data** - configuration for a package
**meta file** - bestow.yml
**template** - a package file that generates a new file
**transient file** - a file that is generated
**version control** - version control system such as git
**convention** - rules that define system functionality over code

## Solutions

### Bestow package meta data

Packages utilizing bestow create configuration file named `bestow.yml`.

### Bestow templates

Bestow templates address the need to generate new transient content, such as replacing environment variables.

Templates and transient content must co-exist in the same package for stow to function properly.

1. templates generate a new transient file in the same package
2. templates must be ignored by stow
3. templates must be included in version control
4. transient files must be ignored by version control

A stow convention of which files to link can be established using:

- stow cli arguments
- user or per module `.stowrc` configuration
- user `.stow-global-ignore or module `.stow-local-ignore` configuration


A version control convention of which transient files to ignore can be established using a similar approach.  For example in git:

- git cli arguments
- user or module `.gitignore` configuration


### Bestow targeting system

The bestow targeting system address the need to change the stow target directory based on configuration.

This simply adds the appropriate CLI argument to stow, and relies on the operating system and stow for security.

For example:

```yaml
targets:
  - file: "system.conf"
    location: "/etc/package/conf.d/"
```

### Bestow conventions

#### Subdirectory Ignore

Create a sub directory pattern ignored by stow to contain meta data and templates.

For example: `<package>/bestow`

Template outputs would then be relative paths back to the package. 

For example:

```yaml
templates:
  - file: "settings.json"
    location: "../module/settings.json"
```

Advantage would be that multiple templates and meta data are isolated with one rule.

#### File Extension Ignore

Ignore a file extension for templates in stow.

For example: `<package>/*.tmpl`

## Example Package Meta File

```yaml
version: "0.0.1"
templates:
  - file: "settings.json.tmpl"
    location: "settings.json"
  - file: "module.conf.tmpl"
    location: "module.conf"
targets:
  - file: "settings.json"
    location: "/etc/package/conf.d/"
  - file: "module.conf"
    location: "/etc/package/conf.d/"
```
