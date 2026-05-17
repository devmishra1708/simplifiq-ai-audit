import { useState } from "react";
import axios from "axios";

function App() {
  const [loading, setLoading] = useState(false);

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    company_name: "",
    website: "",
    industry: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/leads/submit/",
        formData
      );

      alert(response.data.message);

      setFormData({
        name: "",
        email: "",
        company_name: "",
        website: "",
        industry: "",
      });
    } catch (error) {
  console.error(error);

  alert(
    error.response?.data?.error ||
    error.message ||
    "Submission failed"
  );
}

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-black text-white">
      {/* HERO SECTION */}
      <div className="max-w-7xl mx-auto px-6 py-16">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          
          {/* LEFT CONTENT */}
          <div>
            <div className="inline-block px-4 py-2 rounded-full bg-gray-900 border border-gray-800 mb-6">
              AI-Powered Business Intelligence
            </div>

            <h1 className="text-5xl lg:text-7xl font-bold leading-tight">
              Instant AI Audit
              <span className="text-gray-400"> For Modern Businesses</span>
            </h1>

            <p className="text-gray-400 text-lg mt-6 leading-relaxed">
              Submit your company details and receive a fully personalized
              AI-generated business audit report with growth opportunities,
              automation insights, and strategic recommendations.
            </p>

            <div className="flex gap-6 mt-10">
              <div>
                <h2 className="text-3xl font-bold">500+</h2>
                <p className="text-gray-400">Reports Generated</p>
              </div>

              <div>
                <h2 className="text-3xl font-bold">98%</h2>
                <p className="text-gray-400">Client Satisfaction</p>
              </div>
            </div>
          </div>

          {/* FORM CARD */}
          <div className="bg-[#111111] border border-gray-800 rounded-3xl p-8 shadow-2xl">
            <h2 className="text-3xl font-bold mb-2">
              Generate Your AI Audit
            </h2>

            <p className="text-gray-400 mb-8">
              Receive a curated business analysis report directly in your inbox.
            </p>

            <form onSubmit={handleSubmit} className="space-y-5">

              <input
                type="text"
                name="name"
                placeholder="Your Name"
                value={formData.name}
                onChange={handleChange}
                className="w-full bg-black border border-gray-700 rounded-xl p-4 outline-none focus:border-white"
                required
              />

              <input
                type="email"
                name="email"
                placeholder="Business Email"
                value={formData.email}
                onChange={handleChange}
                className="w-full bg-black border border-gray-700 rounded-xl p-4 outline-none focus:border-white"
                required
              />

              <input
                type="text"
                name="company_name"
                placeholder="Company Name"
                value={formData.company_name}
                onChange={handleChange}
                className="w-full bg-black border border-gray-700 rounded-xl p-4 outline-none focus:border-white"
                required
              />

              <input
                type="text"
                name="website"
                placeholder="Company Website"
                value={formData.website}
                onChange={handleChange}
                className="w-full bg-black border border-gray-700 rounded-xl p-4 outline-none focus:border-white"
                required
              />

              <input
                type="text"
                name="industry"
                placeholder="Industry"
                value={formData.industry}
                onChange={handleChange}
                className="w-full bg-black border border-gray-700 rounded-xl p-4 outline-none focus:border-white"
              />

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-white text-black font-semibold py-4 rounded-xl hover:bg-gray-200 transition-all duration-300"
              >
                {loading ? "Generating Audit..." : "Generate AI Audit"}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;