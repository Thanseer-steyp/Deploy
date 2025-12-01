"use client";
import { useEffect, useState } from "react";
import axios from "axios";
import axiosInstance from "@/components/config/AxiosInstance";

export default function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Load Razorpay script
    const script = document.createElement("script");
    script.src = "https://checkout.razorpay.com/v1/checkout.js";
    script.async = true;
    document.body.appendChild(script);
  }, []);

  useEffect(() => {
    const token = localStorage.getItem("access");

    axiosInstance
      .get("user/products/")
      .then((res) => setProducts(res.data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2 className="text-center text-xl">Products</h2>
      {products.map((p) => (
        <div key={p.id} className="border border-white w-max p-2 bg-amber-100">
          <h3 className="text-black text-center text-lg">{p.name}</h3>
          <h3 className="text-black text-center text-lg">₹{p.price}</h3>
          <img src={p.image} className="w-24" alt="" />

          <button
            onClick={() => purchase(p.id)}
            className="p-1 bg-amber-600 mx-auto w-full block"
          >
            Buy
          </button>
        </div>
      ))}
    </div>
  );
}

// --- Purchase function ---
async function purchase(productId) {
  const token = localStorage.getItem("access");

  const res = await axiosInstance.post(
    "user/create-order/",
    { product_id: productId },
    {
      headers: { Authorization: `Bearer ${token}` },
    }
  );

  const options = {
    key: res.data.key,
    amount: res.data.amount,
    order_id: res.data.order_id,

    handler: async function (response) {
      await axiosInstance.post("user/verify-payment/", response, {
        headers: { Authorization: `Bearer ${token}` },
      });

      alert("Payment Successful!");
    },
  };

  if (!window.Razorpay) {
    alert("Razorpay SDK failed to load. Check your internet.");
    return;
  }

  const rzp = new window.Razorpay(options);
  rzp.open();
}
