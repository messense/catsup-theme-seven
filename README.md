Seven
=============

Overview
--------------

A responsive designed theme for [catsup](https://github.com/whtsky/catsup).
It's designed by [Messense](https://github.com/messense).

Installation
--------------

Requires catsup 0.0.6+

The easy way using `catsup install` :
```bash
cd /path/to/your/blog
catsup install https://github.com/messense/catsup-theme-seven.git
```

The hard way using git manually:
```bash
cd /path/to/your/blog
mkdir themes
cd themes
git clone https://github.com/messense/catsup-theme-seven.git
mv catsup-theme-seven seven
```

Configuration
--------------
Edit your configuration file, change `theme.name` to `seven`

Customize
--------------
You can customize your theme by changin `theme.vars`

+ Change blog description
```json
{
    "theme": {
        "name": "seven",
        "vars": {
            "description": "description here",
        }
    }
}
```

+ Add links in footer
```json
{
    "theme": {
        "name": "seven",
        "vars": {
            "links": [
                {
                    "name": "catsup",
                    "url": "https://github.com/whtsky/catsup",
                    "description": "Awesome!"
                }
            ]
        }
    }
}
```