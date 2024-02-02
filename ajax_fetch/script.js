// const products = document.querySelector('#products')
// const url = 'http://127.0.0.1:8000/shop/api/orders/'
//
// axios({
//     method : 'POST',
//     url : url,
//     // data :{ // for post
//     //     firstName : 'Armin'
//     // },
//     // params : { // for get
//     //     key1: 'value1',
//     //     key2: 'value2'
//     // }
//
//
// }).then(function (response) {
//         // handle success
//         // console.log(response.data);
//         response.data.forEach(order => {
//             const orderDiv = document.createElement('div');
//             orderDiv.innerHTML = `<h2>Order ID: ${order.id}<br>${order.order_date}</h2>`;
//             const productList = document.createElement('ul');
//             console.log(order)
//             productTitle = document.createElement('h3')
//             productTitle.innerHTML = 'products'
//             productList.appendChild(productTitle)
//             order.ordered_products.forEach(product => {
//                 const productItem = document.createElement('li');
//                 productItem.innerHTML = `<strong>${product.name}</strong> - ${product.description} - $${product.price}`;
//                 productList.appendChild(productItem);
//             });
//
//             orderDiv.appendChild(productList);
//             document.body.appendChild(orderDiv);
//
//         })
//     })
//     .catch(function (error) {
//         // handle error
//         console.log(error);
//     })
//     .finally(function () {
//         // always executed
//     });




// fetch(url)
//     .then((response) => {
//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }
//         console.log(response)
//         return response.json();
//     })
//     .then((response) => {
//         response.forEach(order => {
//         const orderDiv = document.createElement('div');
//         orderDiv.innerHTML = `<h2>Order ID: ${order.id}<br>${order.order_date}</h2>`;
//         const productList = document.createElement('ul');
//             console.log(order)
//             productTitle = document.createElement('h3')
//             productTitle.innerHTML = 'products'
//             productList.appendChild(productTitle)
//             order.ordered_products.forEach(product => {
//                 const productItem = document.createElement('li');
//                 productItem.innerHTML = `<strong>${product.name}</strong> - ${product.description} - $${product.price}`;
//                 productList.appendChild(productItem);
//             });
//
//             orderDiv.appendChild(productList);
//             document.body.appendChild(orderDiv);
//
//         })
//
//     })




axios({
    method : 'post',
    url : 'http://127.0.0.1:8000/shop/api/addresses/',
    data : {
        "customer_name":
            "Iman 2"
        ,
        "address_line_1":
            "Beheshti"
        ,
        "city":
            "Tehran"
        ,
        "state":
            "Tehran"
        ,
        "zip_code":
            "444"
    },
    headers :{
        'Content-Type': 'application/json'
    }
}).then(function (response) {
    // handle success
    // console.log(response.data);
    console.log(response.data)
})
    .catch(function (error) {
        // handle error
        console.log(error);
    })
    .finally(function () {
        // always executed
    });