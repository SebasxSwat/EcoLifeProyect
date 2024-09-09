"use client";

import { GoogleOAuthProvider } from "@react-oauth/google";
import { SidebarDemoUser } from "@/components/user/SidebarDemo-User";

export default function Home() {
  return (
    <GoogleOAuthProvider clientId="YOUR_GOOGLE_CLIENT_ID">
      <SidebarDemoUser/>
    </GoogleOAuthProvider>
  );
}
