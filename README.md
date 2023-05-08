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
    Modern Python client for interacting with the Plunet SOAP 3.0 API.
    <br />


  </p>
</div>


<!-- ABOUT THE PROJECT -->

## About The Project
Modern Python client for interacting with the Plunet SOAP API, without having to deal with any of the soapiness.

Ready to use out of the box, you can jump directly into the business logic. 

Pip install, import and start working. It really is as easy as that! 

- Implements all services and methods as per Plunet 9.2 (the latest version of ApiDocs available)
- Fully typed for validation and code completion support
- Fully documented methods with complete content of the Plunet JavaDocs.

<p align="right">(<a href="#top">back to top</a>)</p>

### New in 0.7.0
- Retrying client that uses tenacity to retry on ConnectionError from zeep/requests
- Improved typing for enums - all are still not covered but getting there

### Built With

* [zeep](https://docs.python-zeep.org/en/master/)
* [pydantic](https://docs.pydantic.dev/)
* [plunetapi](https://github.com/kuhnemann/plunetapi/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

### Installation


Install via pip

   ```sh
   pip install pyplunet
   ```

To include tenacity:
   ```sh
   pip install pyplunet[retry] 
   ```

Or clone the repo

   ```sh
   git clone https://github.com/kuhnemann/pyplunet.git
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

Install using pip like so:

```sh
pip install pyplunet
```

Initialize the client with the base URL of your Plunet instance, authenticate and start doing whatever you aim to do.


```sh
from pyplunet import PlunetClient


plunet_client = PlunetClient(base_url="YOUR_URL")

plunet_client.login(username=username, password=password)

order_result = plunet_client.order.get_order_object(order_id=1234)
```


Complex types and enums are included. Convenient when searching or creating entities:

```sh
from datetime import datetime, timedelta

from pyplunet import PlunetClient
from pyplunet.models import OrderIN, SearchFilter_Resource
from pyplunet.enums import ResourceType, ResourceStatus, WorkingStatus


plunet_client = PlunetClient(base_url="YOUR_URL")

plunet_client.login(username=username, password=password)

# prepare the searchfilter
sf_resource = SearchFilter_Resource(
    contact_resourceID=-1,
    languageCode="EN",
    resourceType=ResourceType.PROJECT_MANAGER,
    resourceStatus=ResourceStatus.ACTIVE,
    workingStatus=WorkingStatus.INTERNAL
)
# get the result
pms_result = plunet_client.resource.search(search_filter_resource=sf_resource)

# prepare the OrderIN object. Fields are typed and corresponds to definition from XSD.
order_in = OrderIN(
    currency="SEK",
    customerContactID=1,
    customerID=3,
    deliveryDeadline=datetime.now() + timedelta(days=7),
    orderDate=datetime.now(),
    orderID=-1,
    projectManagerID=11,
    projectManagerMemo="Some memo!",
    projectName="Project has a name",
    rate=-1,
    referenceNumber="This is the reference number",
    subject="This is the subject!"
)
order_integer_result = plunet_client.order.insert2(order_in=order_in)
order_id = order_integer_result.data
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