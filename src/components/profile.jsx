// components/ProfilePictureUpload.jsx
import React, { useState } from 'react';

export default function ProfilePictureUpload() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const handleUpload = async () => {
    if (selectedImage) {
      // Lógica para subir la imagen a tu servidor o almacenamiento
      const formData = new FormData();
      formData.append('file', selectedImage);

      // Ejemplo de cómo podrías enviar la imagen a tu API
      await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });

      // Aquí podrías manejar la respuesta del servidor y actualizar el estado
    }
  };

  return (
    <div className="flex flex-col items-center">
      <div className="w-32 h-32 mb-4">
        {preview ? (
          <img src={preview} alt="Preview" className="w-full h-full object-cover rounded-full" />
        ) : (
          <div className="w-full h-full bg-gray-200 rounded-full flex items-center justify-center">
            <span className="text-gray-600">No image selected</span>
          </div>
        )}
      </div>
      <input
        type="file"
        accept="image/*"
        onChange={handleImageChange}
        className="mb-4"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        Upload
      </button>
    </div>
  );
}
