function Input({
    label,
    name,
    type = "text",
    error,
    ...props
  }) {
    return (
      <div className="flex flex-col gap-2">
        <label
          htmlFor={name}
          className="text-sm font-semibold text-slate-700"
        >
          {label}
        </label>
  
        <input
          id={name}
          name={name}
          type={type}
          className={`
            w-full
            rounded-xl
            bg-white/80
            px-4
            py-3
            text-base
            text-slate-900
            placeholder:text-slate-400
            shadow-sm
            outline-none
            transition-all
            duration-200
            ${
              error
                ? "border border-red-500 focus:border-red-500 focus:ring-4 focus:ring-red-200"
                : "border border-slate-300 focus:border-blue-500 focus:ring-4 focus:ring-blue-200"
            }
          `}
          {...props}
        />
  
        {error && (
          <p className="text-sm font-medium text-red-600">
            {error.message}
          </p>
        )}
      </div>
    );
  }
  
  export default Input;