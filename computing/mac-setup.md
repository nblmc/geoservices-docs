# Setting up a Mac for geospatial computing

## Installing Homebrew

**Homebrew** is a *package manager* for macOS—a system for installing, upgrading, and uninstalling *packages* and their *dependencies*. Anything that you install with Homebrew you could, if you wanted to, install by hand, but you'd have a real headache making sure everything was in the correct place. For instance, the `gdal` package has about two dozen dependencies, like `proj`, `libgeotiff`, and so on, which you'd have to make sure were in place for `gdal` to access. Homebrew does all this for you (or, at least it does most of the time).

The installation instructions for Homebrew can be found at <https://brew.sh>. You can install Homebrew without downloading anything from the browser by running the following command in Terminal:

```shell
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Everything that Homebrew install goes into the `/usr/local`, so if you later need to wipe everything out and start again, you can delete that directory and its contents.

To make sure that Homebrew is running correctly, run:

```shell
$ brew doctor
```

The most important commands in Homebrew are:

```shell
$ brew install [package]
$ brew uninstall [package]	
$ brew reinstall [package]
```

To update Homebrew's list of packages:

```shell
$ brew update
```

And to upgrade an already installed package:

```shell
$ brew upgrade [package]
```



## Installing Homebrew's Python

macOS comes bundled with a preinstalled version of Python, currently 2.7.10. If you run `which python` from the Terminal, you should get `/usr/bin/python`, which is the preinstalled Python; try `python --version` to check which version this is.

It's preferable to use Homebrew installed versions of Python for active development work, because you can then use Homebrew to install necessary Python packages, and anything else that you install with Homebrew will bind and compile against these versions of Python.

Run the following to install a Homebrew Python 2 (the @ sign is used for specifying a release):

```shell
$ brew install python@2
```

And then to install Python 3:

```shell
$ brew install python@3
```

Homebrew should also install corresponding versions of `pip` for you. To check that everything is correct, try the following commands, which should respond in this way:

```shell
$ which python
> /usr/local/bin/python
$ which pip
> /usr/local/bin/pip
$ which python3
> /usr/local/bin/python3
$ which pip3
> /usr/local/bin/pip3
```

See how everything is in `/usr/local`? That's as it should be.

### A note about pip and Homebrew

There are some Python packages which can be installed by *both* pip and Homebrew. In most cases, it's better to install via Homebrew, though, if you're finding that you only have a package installed for Python 2 or Python 3, you can try also installing with pip.

## Installing geospatial packages

Homebrew has several hundred packages (called *formulae*) that it knows how to install on its own; see <https://formulae.brew.sh/formula/> for a list.

You can also connect Homebrew to additional libraries of packages using what are called *taps*. OSGeo4Mac maintains a tap of geospatial software, which you can add to Homebrew by running `$ brew tap osgeo/osgeo4mac`. Note that this only adds the *ability* to install packages from the OSGeo4Mac repository—you haven't actually installed any packages by running this command.

### A note about OSGeo4Mac tap formulae

There are some formulae in the OSGeo4Mac tap that *also* exist in Homebrew's core repository. This can get confusing: for instance, if you run `$ brew install gdal`, you'll install the Homebrew core formula of `gdal` (currently v2.4.2), whereas if you run `$ brew install osgeo-gdal` , you'll install the `gdal` from the OSGeo4Mac tap (currently v3.0.1). 

### Recommended packages to install with Homebrew

The following packages are useful to install for geospatial computing, using the `$ brew install` command:

- `osgeo-gdal`
  - Dependencies of this package which will be auto-installed include `osgeo-proj`, `osgeo-postgresql`, `numpy`
- `node`
- `imagemagick`
- `ffmpeg`

### Recommended packages to install with pip

These packages are useful for Python processing. You should install with `pip` or `pip3`, depending on whether you want to work in Python 2 or Python 3, respectively.

- `shapely`
- `fiona`
- `geopandas`

## Installing QGIS

There are two ways to get QGIS on a Mac: installing the app bundle, or installing via Homebrew. The advantage to installing the app bundle is that it behaves much more like a normal Mac app, and is self-contained. The disadvantage is that the app bundle contains its own versions of libraries like `proj`, `gdal`, and so on, which means you're both installing duplicate versions of these libraries, and will also have difficulty accessing those libraries from *outside* of the app bundle. The advantage of installing QGIS from Homebrew is that it builds against the Homebrew-installed versions of these libraries, and therefore keeps all your geospatial software within one ecosystem. However, the Homebrew formula for QGIS is also more fragile, and, if you update one of the dependencies at a time when the Homebrew QGIS formula isn't yet ready for those newer versions of the dependencies, you'll break QGIS.

### From the app bundle

This is the easy way: go to <https://qgis.org/en/site/forusers/download.html>, download, and install. You now have a normal QGIS app that you can click on and open.

### From Homebrew

First, run `$ ulimit -n 1024`, since Homebrew is such a large package that it will want to open more files during installation than Ruby will otherwise allow. Then run  `$ brew install osgeo-qgis`. You may get errors stating that you need to install dependencies like `xquartz`. If so, run the command that the installer suggests. 

### From Homebrew Cask

There's a third option, which is really just a command line wrapper around the first version. Homebrew has a feature called Casks, which is nothing more than a command line tool to download, open, and install app bundles from a `.dmg` file. Essentially, it does exactly the same thing that you would do by download an installer from the browser, opening it, dragging the application to your hard drive, and then deleting the installer file. To install the QGIS bundle in this way, run `$ brew cask install qgis`