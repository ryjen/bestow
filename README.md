# bestow

A casing for [GNU stow](https://linux.die.net/man/8/stow) to add templating.

## Goals

1. Allow environment variables in stowed content

### Terminology

- **stow** - GNU stow utility
- **package** - a directory being stowed
- **meta data** - configuration for a package
- **meta file** - bestow.yml
- **template** - a package file that generates a new file
- **transient file** - a file that is generated
- **version control** - version control system such as git
- **convention** - rules that define system functionality over code

## Solutions

### Package Meta Data:

Stow packages utilizing bestow create a configuration file named `bestow.yml`.

### Templates:

Bestow templates address the need to add transient content, such as environment specific variables.

Templates and generated content must co-exist in the same package for stow to function properly.

1. templates generate a new transient files in the same package
2. templates must be ignored by stow
3. templates must be included in version control
4. transient files must be ignored by version control

Stow conventions of which files should ignored can be established using:

- stow command line arguments (passthrough)
- user or per package `.stowrc` configuration
- user `.stow-global-ignore` or package `.stow-local-ignore` configuration

Version control conventions of which transient files to ignore can be established using a similar approach.  For example in git:

- git command line arguments
- user or package `.gitignore` configuration

## Conventions:

### Subdirectory Ignore:

**1.** Add a directory pattern to stow using `~/.stow-global-ignore` or `<package>/.stow-local-ignore`:

```
_meta
```

**2.** Configure `<package>/_meta/bestow.yml`.  Template outputs are relative paths back to the package: 

```yaml
version: "0.0.1"
templates:
  - file: "settings.json"
    location: "../module/settings.json"
```

**3** Add transient files to version control ignore lists (`.gitignore`):

```
module/settings.json
```


### File Ignore:

**1.** Add a file pattern to `.stow-global-ignore` or `<package>/.stow-local-ignore`:

```
*.tmpl
bestow.yml
```

**2.** Configure `<package>/bestow.yml`:

```yaml
version: "0.0.1"
templates:
  - file: "settings.json.tmpl"
    location: "settings.json"
  - file: "module.conf.tmpl"
    location: "module.conf"
```

**3.** Add transient files to version control ignore lists (`<package>/.gitignore`):

```
/module.conf
/settings.json
```

## TODO

- [ ] refactor prototype in a non-script language
- [ ] automagically handle stow ignore configuration
- [ ] automagically handle version control configuration
- [ ] add version check


## Related

- [GNU stow](https://linux.die.net/man/8/stow)
- [envsubst](https://linux.die.net/man/1/envsubst)
- [dotfile managers](https://github.com/topics/dotfile-manager)
