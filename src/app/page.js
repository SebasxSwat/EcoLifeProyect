"use client";

import { GoogleOAuthProvider } from "@react-oauth/google";
import { SidebarDemo } from "@/components/admin/SidebarDemo";

export default function Home() {
  return (
    <GoogleOAuthProvider clientId="YOUR_GOOGLE_CLIENT_ID">
      <SidebarDemo/>
    </GoogleOAuthProvider>
  );
}
