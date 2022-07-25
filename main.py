import firstsdk as sdk


def main():
    rates = sdk.get_shipments_rates()
    print(rates)

if __name__ == '__main__':
    main()