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
