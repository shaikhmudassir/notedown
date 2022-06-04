# Documentation

## Basic Usage
* Click on **Create New** Button to create new note.
* Click on **Yellow** Button given in each note to **Edit** that note.
* Click on **Red** Button given in each note to **Delete** that note.
* To add **Tag** into your note use the following syntax
	> \`@tag_name\`
	>
	> (  **\`**  ) This is **Grave Accent** symbol not a single quote
	>
	> which is located directly below the **Esc** key.
	
---

# Markdown Guide
```
  # h1 Heading
  ## h2 Heading
  ### h3 Heading
  #### h4 Heading
  ##### h5 Heading
  ###### h6 Heading
```
Output : 
> # h1 Heading
> ## h2 Heading
> ### h3 Heading
> #### h4 Heading
> ##### h5 Heading
> ###### h6 Heading
---

## Emphasis
```
  **This is bold text** 

  __This is bold text__

  *This is italic text*

  _This is italic text_

  ~~Strikethrough~~
```
Output :
> **This is bold text**
> 
> __This is bold text__
> 
> *This is italic text*
> 
> _This is italic text_
> 
> ~~Strikethrough~~
---

## Lists
#### Unordered
```
+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!
```
Output :
> + Create a list by starting a line with `+`, `-`, or `*`
> + Sub-lists are made by indenting 2 spaces:
>   - Marker character change forces new list start:
>     * Ac tristique libero volutpat at
>     + Facilisis in pretium nisl aliquet
>     - Nulla volutpat aliquam velit
> + Very easy!
---

#### Ordered
```
1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

Start numbering with offset:

57. foo
1. bar
```
Output :
> 1. Lorem ipsum dolor sit amet
> 2. Consectetur adipiscing elit
> 3. Integer molestie lorem at massa
> 
> 1. You can use sequential numbers...
> 1. ...or keep all the numbers as `1.`
> 
> Start numbering with offset:
> 
> 57. foo
> 1. bar
---

## Code
```
Inline `code`
```
Output : 
> Inline `code`
---

#### Indented code
``````
  ```
  // Some comments
  IF (TRUE)
  {
    // Code
  }
 ```
``````
Output :
> ```
>   // Some comments
>   IF (TRUE)
>   {
>     // Code
>   }
> ```
---
#### Syntax highlighting
``````
``` js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```
``````
Output :
> ``` js
> var foo = function (bar) {
>   return bar++;
> };
> 
> console.log(foo(5));
> ```

#### Tables
```
| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
```

> | Option | Description |
> | ------ | ----------- |
> | data   | path to data files to supply the data that will be passed into templates. |
> | engine | engine to be used for processing templates. Handlebars is the default. |
> | ext    | extension to be used for dest files. |

Right aligned columns
```
| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
```
> | Option | Description |
> | ------:| -----------:|
> | data   | path to data files to supply the data that will be passed into templates. |
> | engine | engine to be used for processing templates. Handlebars is the default. |
> | ext    | extension to be used for dest files. |

#### Links
```
[link text](http://dev.nodeca.com)

[link with title](http://nodeca.github.io/pica/demo/ "title text!")
```
Output :
> [link text](http://dev.nodeca.com)
> 
> [link with title](http://nodeca.github.io/pica/demo/ "title text!")

#### Emojies
```
Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum:

Shortcuts (emoticons): :-) :-( 8-) ;)
```
> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum:
>
> Shortcuts (emoticons): :-) :-( 8-) ;)

