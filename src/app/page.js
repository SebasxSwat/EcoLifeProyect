"use client";

import { SidebarDemo } from "@/components/features/SidebarDemo";
import { GoogleOAuthProvider } from "@react-oauth/google";
import { AdminUserList } from "@/components/pages/admin/admin-user-list";

export default function Home() {
  return (
    <GoogleOAuthProvider clientId="YOUR_GOOGLE_CLIENT_ID">
      <SidebarDemo/>
    </GoogleOAuthProvider>
  );
}
