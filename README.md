<div id="top"></div>


<!-- PROJECT SHIELDS -->


[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->


<h3 align="center">PyPlunet</h3>

  <p align="center">
    Client for interacting with the Plunet SOAP 3.0 API.
    <br />


  </p>
</div>







<!-- ABOUT THE PROJECT -->

## About The Project

Work in progress. Methods will be implemented irregularly and as need arise. Feel free to contribute!  

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [zeep](https://docs.python-zeep.org/en/master/)
* [plunetapi](https://github.com/kuhnemann/plunetapi/)
* [Plunet](https://www.plunet.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

### Installation

Clone the repo

   ```sh
   git clone https://github.com/kuhnemann/pyplunet.git
   ```

Or install via pip

   ```sh
   pip install pyplunet
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

Install using pip like so:

```sh
pip install pyplunet
```

Initialize the client with the base URL of your Plunet instance, authenticate and start doing whatever you aim to do.

API is likely to change, so remember to pin version if you use this for something important.


```sh
from pyplunet import PlunetClient


plunet_client = PlunetClient(base_url="YOUR_URL")

plunet_client.login(username=username, password=password)

print(plunet_client.order.get_order_object(order_id=1234))


```



<p align="right">(<a href="#top">back to top</a>)</p>




See the [open issues](https://github.com/kuhnemann/pyplunet/issues) for a full list of proposed features (and known
issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

Henrik Kühnemann - [@hkuhnemann](https://twitter.com/hkuhnemann) - [hello@yellownape.se](mailto:hello@yellownape.se)

Project Link: [https://github.com/kuhnemann/pyplunet](https://github.com/kuhnemann/pyplunet)

<p align="right">(<a href="#top">back to top</a>)</p>



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/kuhnemann/pyplunet.svg?style=for-the-badge

[contributors-url]: https://github.com/kuhnemann/pyplunet/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/kuhnemann/pyplunet.svg?style=for-the-badge

[forks-url]: https://github.com/kuhnemann/pyplunet/network/members

[stars-shield]: https://img.shields.io/github/stars/kuhnemann/pyplunet.svg?style=for-the-badge

[stars-url]: https://github.com/kuhnemann/pyplunet/stargazers

[issues-shield]: https://img.shields.io/github/issues/kuhnemann/pyplunet.svg?style=for-the-badge

[issues-url]: https://github.com/kuhnemann/pyplunet/issues

[license-shield]: https://img.shields.io/github/license/kuhnemann/pyplunet.svg?style=for-the-badge

[license-url]: https://github.com/kuhnemann/pyplunet/blob/main/LICENCE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/henrik-kuhnemann

[product-screenshot]: images/screenshot.png