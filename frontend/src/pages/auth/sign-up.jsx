"use client";

import { GoogleLogin } from "@react-oauth/google";

export default function SignUp() {
  const handleLoginSuccess = (response) => {
    console.log(response);
    // Manejar el token y el inicio de sesión
  };

  const handleLoginError = (error) => {
    console.error(error);
    // Manejar el error
  };

  return (
    <div className="bg-gradient-to-t from-gray-700 via-gray-900 to-black w-full h-screen flex flex-col lg:flex-row">
      {/* Contenedor del formulario */}
      <div className="flex flex-col items-start justify-center w-full lg:w-1/2 px-4 py-8 lg:pl-52">
        <h1 className="text-4xl font-bold text-white mb-12">Sign Up</h1>
        <div className="mb-6">
          <GoogleLogin
            onSuccess={handleLoginSuccess}
            onError={handleLoginError}
            theme="filled_blue"
            size="large"
            className="custom-google-login w-full bg-transparent border border-gray-400 text-gray-400 py-2 px-4 rounded-lg flex items-center justify-start space-x-2 hover:scale-105 duration-300"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 48 48"
              className="w-5 h-5"
            >
              <path
                d="M23.49 12.27c-.78 0-1.54-.07-2.28-.2L12 20.66l5.68 3.78c3.31-3.08 5.81-7.46 6.81-12.17z"
                fill="#4285F4"
              />
              <path
                d="M12 4.09c-3.76 0-7.26 1.27-10.1 3.43L1.37 4.34C4.73 1.1 8.84 0 12 0c6.88 0 12.85 2.27 17.78 6.06L17.69 12.25C15.24 10.58 13.13 8.61 12 6.51c-1.16 1.27-2.68 2.17-4.47 2.6l.09-.01z"
                fill="#34A853"
              />
              <path
                d="M12 9.09c-1.8 0-3.48-.64-4.86-1.79L2.5 12.39c1.24 1.56 2.85 2.85 4.65 3.72l-.15.01c2.43 0 4.66-.83 6.48-2.22l-5.28-3.41c-1.29.63-2.75 1.01-4.32 1.01z"
                fill="#FBBC05"
              />
              <path
                d="M12 20.66c-2.1 0-4.03-.68-5.64-1.82L2.57 21.5c2.69 2.64 6.25 4.5 10.21 4.5 6.91 0 12.92-2.35 17.9-6.3l-6.38-4.16c-2.92 2.13-6.79 3.46-10.65 3.46z"
                fill="#EB4335"
              />
            </svg>
          </GoogleLogin>
        </div>
        <div className="mt-8 w-3/4">
          <label htmlFor="email" className="block text-slate-300 mb-2">
            Email
          </label>
          <input
            id="email"
            type="text"
            placeholder="example: email@gmail.com"
            className="w-full bg-transparent border border-gray-400 py-2 px-4 rounded-lg focus:outline-none focus:border-gray-600"
          />
        </div>
        <div className="mt-8 w-3/4">
          <label htmlFor="password" className="block text-slate-300 mb-2">
            Password
          </label>
          <input
            id="password"
            type="password"
            placeholder="********"
            className="w-full bg-transparent border border-gray-400 py-2 px-4 rounded-lg focus:outline-none focus:border-gray-600"
          />
        </div>
        <div className="mt-8 w-3/4">
          <label
            htmlFor="repeat-password"
            className="block text-slate-300 mb-2"
          >
            Repeat Password
          </label>
          <input
            id="repeat-password"
            type="password"
            placeholder="********"
            className="w-full bg-transparent border border-gray-400 py-2 px-4 rounded-lg focus:outline-none focus:border-gray-600"
          />
        </div>
        <div className="mt-8 w-3/4">
          <button className="w-full bg-blue-600 text-white text-lg font-bold py-2 px-4 rounded-lg hover:bg-blue-800 duration-300">
            Sign Up
          </button>
        </div>
        <div className="mt-8 w-full max-w-xs flex">
          <label htmlFor="have-account" className="block text-slate-300 mb-2">
            Have an account?
          </label>
          <a href="/" className="text-blue-500 hover:underline ml-4">
            Sign In
          </a>
        </div>
      </div>

      {/* Contenedor de la imagen */}
      <div className="w-full lg:w-1/2 h-full flex items-center justify-center">
        <div className="relative w-11/12 h-5/6 overflow-hidden rounded-lg mr-40">
          <img
            src="/imgs/fondo2.jpg"
            alt="Background"
            className="absolute inset-0 w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-black bg-opacity-50"></div>
          <div className="relative z-10 p-8 text-white">
            <h1 className="text-5xl font-bold mb-16 my-16">
              Register in EcoLife and start having a more sustainable life
            </h1>
            <p className="text-lg text-slate-200">
              Create your account and start improving your lifestyle
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
