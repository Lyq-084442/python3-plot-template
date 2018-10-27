#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd

# line styles
styles = [
    {
        'color': '#a00000',
        'ls': '-',
        'marker': 'o',
        'markevery': 1,
        'markersize': 12,
        'markerfacecolor': 'None',
    },
    {
        'color': '#00a000',
        'ls': '-',
        'marker': 'x',
        'markevery': 1,
        'markerfacecolor': 'None',
    },
    {
        'color': '#5060d0',
        'ls': '-',
        'marker': '>',
        'markersize': 12,
        'markevery': 1,
    },
    {
        'color': '#f25900',
        'ls': '-',
        'marker': 'd',
        'markevery': 3,
        'markerfacecolor': 'None',
    },
    {
        'color': '#500050',
        'ls': '*',
        'marker': 'd',
        'markevery': 1,
        'markerfacecolor': 'None',
    }
]


def main():
    df = pd.read_csv(
        'data.csv',
        sep=r'\s+',
        names=('x', 'y'),
        usecols=(0, 1),
    )
    # plt.style.use('paper')
    fig, ax = plt.subplots()
    ax.plot(df.x, df.y, **styles[0], label='Line')
    ax.minorticks_on()
    ax.grid(axis='both', which='major', ls='dotted', linewidth=2, alpha=0.9)
    ax.grid(axis='both', which='minor', ls='dotted', linewidth=1.5, alpha=0.5)
    ax.legend(loc='best')
    plt.xlabel('x val')
    plt.ylabel('y val')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
