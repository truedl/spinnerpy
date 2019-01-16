# spinnerpy
🔥 Spinnerpy new python loading spinners repository [!]

# Style-list

<table>
  <tr>
    <th>Style</th>
    <th>Chars</th>
  </tr>
  <tr>
    <td>default</td>
    <td>\ | / -</td>
  </tr>
  <tr>
    <td>ballon</td>
    <td>. o 0 @ *</td>
  </tr>
  <tr>
    <td>arrows</td>
    <td>← ↖ ↑ ↗ → ↘ ↓ ↙</td>
  </tr>
  <tr>
    <td>cube</td>
    <td>▖ ▘ ▝ ▗</td>
  </tr>
  <tr>
    <td>lines</td>
    <td>┤ ┘ ┴ └ ├ ┌ ┬ ┐</td>
  </tr>
  <tr>
    <td>tringle</td>
    <td>◢ ◣ ◤ ◥</td>
  </tr>
  <tr>
    <td>squares</td>
    <td>◰ ◳ ◲ ◱</td>
  </tr>
  <tr>
    <td>pie</td>
    <td>◴ ◷ ◶ ◵</td>
  </tr>
  <tr>
    <td>circle</td>
    <td>◐ ◓ ◑ ◒</td>
  </tr>
  <tr>
    <td>dots</td>
    <td>⣾ ⣽ ⣻ ⢿ ⡿ ⣟ ⣯ ⣷</td>
  </tr>
  <tr>
    <td>v</td>
    <td>< V > ^</td>
  </tr>
  <tr>
    <td>x</td>
    <td>+ X</td>
  </tr>
</table>

# Spinner Class

<b>__init__</b>
```
Spinner(style:str)
```

<b>start</b>
```
start(self, progress=None, args:list=None, text:str='', times:int=None, wait:float=.2, color:str=None)
```
<i>Start the spinner</i>

`progress` - `Function` - `(The spinner will spin until the progress is over)`
`args` - `Array` - `(If progress is provided you can transfer arguments to the function)`
`text` - `String` - `(Text before spinner | Example: text='Loading... ' - Output: Loading... {Spinner Here})`
`times` - `Integer` - `(If progress not provided you can control how many times the spinner will spin)`
`wait` - `Float` - `(Seconds to next char)`
`color` - `String` - `(Change spinner+text color)`

<b>stop</b>
```
stop(self)
```
<i>Stop the spinner</i>
