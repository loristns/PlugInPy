          _____  _             _____       _____       
         |  __ \| |           |_   _|     |  __ \      
         | |__) | |_   _  __ _  | |  _ __ | |__) |   _ 
         |  ___/| | | | |/ _` | | | | '_ \|  ___/ | | |
         | |    | | |_| | (_| |_| |_| | | | |   | |_| |
         |_|    |_|\__,_|\__, |_____|_| |_|_|    \__, |
                          __/ |                   __/ |
                         |___/                   |___/ 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/aa9124df47d54202abe4db0ae2f14cec)](https://www.codacy.com/app/lorisazerty/PlugInPy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=the-new-sky/PlugInPy&amp;utm_campaign=Badge_Grade) [![Code Health](https://landscape.io/github/the-new-sky/PlugInPy/master/landscape.svg?style=flat)](https://landscape.io/github/the-new-sky/PlugInPy/master)

The smallest plugin system in Python !

PlugInPy allow you to add a simple Python plugin system to your favorite project. PlugInPy is a plug and play and powerful solution for our small projects. Like all **InPy** softwares, PlugInPy was designed to be very lightweight but extremely powerful.

# Installation

Just clone this repository and look at the documentation.

# Usage

To add a plugin system to your project, add a "plugins" folder in your project directory. This folder contains all plugins you want to add.

## The "Hello-World"

Then, define a default plugin class syntax. Like this :
      
      # Names, methods and parameters of the plugin class need to be identic for every plugin
      class MyProjectPlugin(object):
            """this class say hello to the given name"""
            
            def __init__(self):
                  # In __init__() you can request some plugin variable
                  self.plugin_name = "Hello"
                  
            def run(self, name)
                  # You can define plugins methods
                  print("Hello ", name)

This syntax is universal, for example, this is another plugin applying this syntax :

      class MyProjectPlugin(object):
            """this class say goodbye to the given name"""
            
            def __init__(self):
                  # In __init__() you can request some plugin variable
                  self.plugin_name = "Goodbye"
                  
            def run(self, name)
                  # You can define plugins methods
                  print("Goodbye ", name)

Now, you can create lot of plugin in your plugin directory !

## Execution

Let's see how to execute plugin with PlugInPy !
The only thing you need is a list of every MyProjectPlugin's class in your "plugins" directory. Let's write this :

      from PlugIn import LoadPlugin
      
      loader = LoadPlugin(plugin_dir='plugins') # Say the path to your plugins directory
      loader.import_all() # Import all plugin in this directory
      
      people = input("What's your name ? ")
      
      for plugin in loader.plugins: # For each plugins
            plugin_object = plugin.MyProjectPlugin() # Your plugin is now a simple object
            
            print("The plugin ", plugin_object.plugin_name, "is running...") # You can use it
            plugin_object.run(name=people)


# Me

Created with :heart: in France by **the_new_sky**.
